package dom.com.ssd.ecfx.client.model;
import java.util.Objects; import com.google.gson.*; import com.google.gson.reflect.TypeToken; import com.google.gson.stream.*; import java.io.IOException; import java.util.HashSet;
import dom.com.ssd.ecfx.client.JSON;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", comments = "Generator version: 7.20.0")
public class ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico {
  public ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico() {}
  @Override public boolean equals(Object o) { return this == o || (o != null && getClass() == o.getClass()); }
  @Override public int hashCode() { return Objects.hash(); }
  public static HashSet<String> openapiFields = new HashSet<String>();
  public static HashSet<String> openapiRequiredFields = new HashSet<String>();
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {}
  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked") @Override public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
      if (!ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico.class.isAssignableFrom(type.getRawType())) return null;
      final TypeAdapter<JsonElement> ea = gson.getAdapter(JsonElement.class);
      final TypeAdapter<ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico> ta = gson.getDelegateAdapter(this, TypeToken.get(ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico.class));
      return (TypeAdapter<T>) new TypeAdapter<ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico>() {
        @Override public void write(JsonWriter out, ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico v) throws IOException { ea.write(out, ta.toJsonTree(v).getAsJsonObject()); }
        @Override public ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico read(JsonReader in) throws IOException { return ta.fromJsonTree(ea.read(in)); }
      }.nullSafe();
    }
  }
  public static ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico fromJson(String s) throws IOException { return JSON.getGson().fromJson(s, ImpuestoAdicional2MontoImpuestoSelectivoConsumoEspecifico.class); }
  public String toJson() { return JSON.getGson().toJson(this); }
}
