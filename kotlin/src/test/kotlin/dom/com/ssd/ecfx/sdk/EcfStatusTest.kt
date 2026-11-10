package dom.com.ssd.ecfx.sdk

import dom.com.ssd.ecfx.sdk.infrastructure.Serializer
import dom.com.ssd.ecfx.sdk.models.DgiiSubmissionState
import dom.com.ssd.ecfx.sdk.models.EcfProgress
import dom.com.ssd.ecfx.sdk.models.EcfResponse
import io.kotlintest.shouldBe
import io.kotlintest.specs.ShouldSpec

class EcfStatusTest : ShouldSpec() {
    private fun parse(progress: String, extra: String = ""): EcfResponse {
        EcfJsonDefaults.install()
        // The API omits null values, like the live service does.
        val json = """{"messageId":"00000000-0000-0000-0000-000000000001","timestamp":"2026-11-10T10:00:00Z",""" +
            """"fechaEmision":"2026-11-10","queueName":"ecf-32","includeEcfContent":false,"ecfContent":"",""" +
            """"tipoEcf":"FacturaDeConsumoElectronica","encf":"E320000000001","rncEmisor":"131000001",""" +
            """"montoTotal":118.0,"tenantId":"00000000-0000-0000-0000-000000000002","progress":"$progress",""" +
            """"secuenciaUtilizada":false,"dgiiEnvironment":"Test"$extra}"""
        return Serializer.kotlinxSerializationJson.decodeFromString(EcfResponse.serializer(), json)
    }

    init {
        should("treat NotReceived as terminal and resubmittable") {
            val response = parse("Error", ""","dgiiSubmissionState":"NotReceived","errors":"No recibido"""")
            response.dgiiSubmissionState shouldBe DgiiSubmissionState.NotReceived
            response.estatus shouldBe null
            response.isTerminal shouldBe true
            response.canResubmit shouldBe true
            EcfProcessingException(response).canResubmit shouldBe true
        }
        should("keep polling while PendingReconciliation") {
            val response = parse("UploadedToDgii", ""","estatus":"EnProceso","dgiiSubmissionState":"PendingReconciliation"""")
            response.isPendingReconciliation shouldBe true
            response.isTerminal shouldBe false
        }
        should("tolerate missing, null and unknown states") {
            parse("Finished").dgiiSubmissionState shouldBe null
            parse("Processing", ""","dgiiSubmissionState":null""").isTerminal shouldBe false
            val unknown = parse("Finished", ""","dgiiSubmissionState":"SomeFutureState","someFutureField":1""")
            unknown.dgiiSubmissionState shouldBe null
            unknown.progress shouldBe EcfProgress.Finished
            unknown.isTerminal shouldBe true
        }
        should("not mark rejections as resubmittable") {
            val response = parse("Error", ""","estatus":"Rechazado","dgiiSubmissionState":"Rejected"""")
            response.isTerminal shouldBe true
            response.canResubmit shouldBe false
        }
    }
}
