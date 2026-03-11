/**
 * Configuration for openapi-typescript code generation.
 *
 * Run via: pnpm generate
 *
 * This uses the openapi-typescript CLI directly:
 *   openapi-typescript <spec-path> -o src/generated/v1.d.ts
 *
 * The spec file is located at:
 *   ../ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json
 */
export default {
  input: '../ecf_dgii/src/Apis/ECF_DGII.EcfApi/wwwroot/openapi/v1.json',
  output: 'src/generated/v1.d.ts',
};
