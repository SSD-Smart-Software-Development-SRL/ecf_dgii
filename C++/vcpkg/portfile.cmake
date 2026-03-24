vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO SSD-Smart-Software-Development-SRL/ecf_dgii
    REF "v${VERSION}"
    SHA512 0  # Update with actual SHA512 after release tag is created
    HEAD_REF main
)

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}/C++"
)

vcpkg_cmake_build()
vcpkg_cmake_install()

vcpkg_cmake_config_fixup(
    PACKAGE_NAME ecf-dgii-client
    CONFIG_PATH lib/cmake/ecf-dgii-client
)

file(REMOVE_RECURSE "${CURRENT_PACKAGES_DIR}/debug/include")

vcpkg_install_copyright(FILE_LIST "${SOURCE_PATH}/C++/LICENSE")
