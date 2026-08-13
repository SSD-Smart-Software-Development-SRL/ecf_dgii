from ecf_dgii.frontend_client import EcfFrontendClient


def test_frontend_client_methods() -> None:
    client = EcfFrontendClient(get_token=lambda: "token")

    # Check that only the 6 allowed GET methods exist
    allowed_methods = {
        "query_ecf",
        "search_ecfs",
        "search_all_ecfs",
        "get_ecf_by_id",
        "get_companies",
        "get_company_by_rnc",
        "close",
    }

    methods = [m for m in dir(client) if not m.startswith("_")]
    for m in methods:
        assert m in allowed_methods, f"Method {m} should not be exposed on EcfFrontendClient"
