#include <ecf-dgii-client/EcfClient.h>
#include <ecf-dgii-client/model/ECF.h>
#include <iostream>

int main() {
    // Verify the library links and basic types are usable
    using namespace org::openapitools::client::model;

    auto ecf = std::make_shared<ECF>();
    auto encabezado = std::make_shared<Encabezado>();
    auto idDoc = std::make_shared<IdDoc>();

    auto tipoEcf = std::make_shared<TipoeCFType>();
    tipoEcf->setValue(TipoeCFType::eTipoeCFType::FACTURADECREDITOFISCALELECTRONICA);
    idDoc->setTipoeCF(tipoEcf);

    encabezado->setIdDoc(idDoc);
    ecf->setEncabezado(encabezado);

    std::cout << "ecf-dgii-client package test OK" << std::endl;
    return 0;
}
