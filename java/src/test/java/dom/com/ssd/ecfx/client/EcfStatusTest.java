package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.model.DgiiSubmissionState;
import dom.com.ssd.ecfx.client.model.EcfProgress;
import dom.com.ssd.ecfx.client.model.EcfResponse;
import org.junit.jupiter.api.Test;

import java.io.IOException;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

class EcfStatusTest {

    private static EcfResponse parse(String progress, String extraFields) throws IOException {
        new JSON(); // registers the type adapters
        String json = "{\"messageId\":\"00000000-0000-0000-0000-000000000001\","
                + "\"timestamp\":\"2026-11-10T10:00:00Z\",\"fechaEmision\":\"2026-11-10\","
                + "\"queueName\":\"ecf-32\",\"includeEcfContent\":false,\"ecfContent\":\"\","
                + "\"tipoEcf\":\"FacturaDeConsumoElectronica\",\"encf\":\"E320000000001\","
                + "\"rncEmisor\":\"131000001\",\"rncReceptor\":null,\"montoTotal\":118.0,"
                + "\"fileName\":null,\"tenantId\":\"00000000-0000-0000-0000-000000000002\","
                + "\"estatus\":null,\"codSec\":null,\"fechaFirma\":null,\"mensaje\":null,"
                + "\"errors\":null,\"progress\":\"" + progress + "\",\"emisorReceptorErrors\":null,"
                + "\"secuenciaUtilizada\":false,\"dgiiEnvironment\":\"Test\"" + extraFields + "}";
        return EcfResponse.fromJson(json);
    }

    @Test
    void notReceivedIsTerminalAndResubmittable() throws IOException {
        EcfResponse response = parse("Error", ",\"dgiiSubmissionState\":\"NotReceived\"");
        assertEquals(DgiiSubmissionState.NOT_RECEIVED, response.getDgiiSubmissionState());
        assertTrue(EcfStatus.isTerminal(response));
        assertTrue(EcfStatus.canResubmit(response));
        assertTrue(new EcfClientException("x", null, null, null, response).canResubmit());
    }

    @Test
    void pendingReconciliationKeepsPolling() throws IOException {
        EcfResponse response = parse("UploadedToDgii", ",\"dgiiSubmissionState\":\"PendingReconciliation\"");
        assertTrue(EcfStatus.isPendingReconciliation(response));
        assertFalse(EcfStatus.isTerminal(response));
        assertFalse(EcfStatus.canResubmit(response));
    }

    @Test
    void nullMissingAndUnknownStatesAreTolerated() throws IOException {
        EcfResponse missing = parse("Finished", "");
        assertNull(missing.getDgiiSubmissionState());
        assertTrue(EcfStatus.isTerminal(missing));

        EcfResponse explicitNull = parse("Processing", ",\"dgiiSubmissionState\":null");
        assertNull(explicitNull.getDgiiSubmissionState());
        assertFalse(EcfStatus.isTerminal(explicitNull));

        EcfResponse unknown = parse("Finished", ",\"dgiiSubmissionState\":\"SomeFutureState\",\"someFutureField\":1");
        assertEquals(DgiiSubmissionState.UNKNOWN_DEFAULT_OPEN_API, unknown.getDgiiSubmissionState());
        assertEquals(EcfProgress.FINISHED, unknown.getProgress());
        assertTrue(EcfStatus.isTerminal(unknown));
        assertFalse(EcfStatus.canResubmit(unknown));
    }

    @Test
    void rejectionIsNotResubmittable() throws IOException {
        EcfResponse response = parse("Error", ",\"dgiiSubmissionState\":\"Rejected\"");
        assertTrue(EcfStatus.isTerminal(response));
        assertFalse(EcfStatus.canResubmit(response));
    }
}
