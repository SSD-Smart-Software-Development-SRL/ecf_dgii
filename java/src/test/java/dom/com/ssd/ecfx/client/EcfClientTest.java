package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.model.*;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class EcfClientTest {

    @Test
    public void sendEcf_nullEcf_throwsException() {
        EcfClient client = new EcfClient.Builder()
            .baseUrl("https://api.test.ecfx.ssd.com.do")
            .apiKey("test-token")
            .build();

        EcfClientException ex = assertThrows(EcfClientException.class, () -> {
            client.sendEcf("123456789", null);
        });
        assertTrue(ex.getMessage().contains("must not be null"));
    }

    @Test
    public void sendEcf_nullTipoEcf_throwsException() {
        EcfClient client = new EcfClient.Builder()
            .baseUrl("https://api.test.ecfx.ssd.com.do")
            .apiKey("test-token")
            .build();

        ECF ecf = new ECF();
        Encabezado encabezado = new Encabezado();
        IdDoc idDoc = new IdDoc();
        // tipoeCF left as null
        encabezado.setIdDoc(idDoc);
        ecf.setEncabezado(encabezado);

        EcfClientException ex = assertThrows(EcfClientException.class, () -> {
            client.sendEcf("123456789", ecf);
        });
        assertTrue(ex.getMessage().contains("tipoeCF must not be null"));
    }
}
