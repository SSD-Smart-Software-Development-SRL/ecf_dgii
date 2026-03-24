package dom.com.ssd.ecfx.client.model;
import java.util.Objects; import com.google.gson.*; import com.google.gson.reflect.TypeToken; import com.google.gson.stream.*; import java.io.IOException; import java.util.HashSet;
import dom.com.ssd.ecfx.client.JSON;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", comments = "Generator version: 7.20.0")
public class ImpuestoAdicional2TasaImpuestoAdicional {
  public ImpuestoAdicional2TasaImpuestoAdicional() {}
  @Override public boolean equals(Object o) { return this == o || (o != null && getClass() == o.getClass()); }
  @Override public int hashCode() { return Objects.hash(); }
  public static HashSet<String> openapiFields = new HashSet<String>();
  public static HashSet<String> openapiRequiredFields = new HashSet<String>();
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {}
  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked") @Override public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
      if (!ImpuestoAdicional2TasaImpuestoAdicional.class.isAssignableFrom(type.getRawType())) return null;
      final TypeAdapter<JsonElement> ea = gson.getAdapter(JsonElement.class);
      final TypeAdapter<ImpuestoAdicional2TasaImpuestoAdicional> ta = gson.getDelegateAdapter(this, TypeToken.get(ImpuestoAdicional2TasaImpuestoAdicional.class));
      return (TypeAdapter<T>) new TypeAdapter<ImpuestoAdicional2TasaImpuestoAdicional>() {
        @Override public void write(JsonWriter out, ImpuestoAdicional2TasaImpuestoAdicional v) throws IOException { ea.write(out, ta.toJsonTree(v).getAsJsonObject()); }
        @Override public ImpuestoAdicional2TasaImpuestoAdicional read(JsonReader in) throws IOException { return ta.fromJsonTree(ea.read(in)); }
      }.nullSafe();
    }
  }
  public static ImpuestoAdicional2TasaImpuestoAdicional fromJson(String s) throws IOException { return JSON.getGson().fromJson(s, ImpuestoAdicional2TasaImpuestoAdicional.class); }
  public String toJson() { return JSON.getGson().toJson(this); }
}
