from typing import Any

from ecf_dgii.client import _get_nested


class MockIdDoc:
    def __init__(self, tipoe_cf: str) -> None:
        self.tipoe_cf = tipoe_cf
        self.encf = "E310000000001"


class MockEmisor:
    def __init__(self, rnc: str) -> None:
        self.rnc_emisor = rnc


class MockEncabezado:
    def __init__(self, tipoe_cf: str, rnc: str) -> None:
        self.id_doc = MockIdDoc(tipoe_cf)
        self.emisor = MockEmisor(rnc)


class MockECF:
    def __init__(self, tipoe_cf: str, rnc: str) -> None:
        self.encabezado = MockEncabezado(tipoe_cf, rnc)


def test_get_nested_from_objects() -> None:
    obj = MockECF("FacturaDeCreditoFiscalElectronica", "131460941")
    assert _get_nested(obj, "encabezado", "id_doc", "tipoe_cf") == "FacturaDeCreditoFiscalElectronica"
    assert _get_nested(obj, "encabezado", "emisor", "rnc_emisor") == "131460941"


def test_get_nested_from_dict() -> None:
    payload: dict[str, Any] = {
        "encabezado": {
            "idDoc": {"tipoeCF": "FacturaDeConsumoElectronica", "encf": "E320000000002"},
            "emisor": {"rncEmisor": "987654321"},
        }
    }
    assert _get_nested(payload, "encabezado", "id_doc", "tipoe_cf") == "FacturaDeConsumoElectronica"
    assert _get_nested(payload, "encabezado", "emisor", "rnc_emisor") == "987654321"
