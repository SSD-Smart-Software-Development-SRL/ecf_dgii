package dom.com.ssd.ecfx.client.model;
import java.util.Objects; import com.google.gson.*; import com.google.gson.reflect.TypeToken; import com.google.gson.stream.*; import java.io.IOException; import java.util.HashSet;
import dom.com.ssd.ecfx.client.JSON;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", comments = "Generator version: 7.20.0")
public class InformacionesAdicionales {
  public InformacionesAdicionales() {}
  @Override public boolean equals(Object o) { return this == o || (o != null && getClass() == o.getClass()); }
  @Override public int hashCode() { return Objects.hash(); }
  public static HashSet<String> openapiFields = new HashSet<String>();
  public static HashSet<String> openapiRequiredFields = new HashSet<String>();
  public static void validateJsonElement(JsonElement jsonElement) throws IOException {}
  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked") @Override public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
      if (!InformacionesAdicionales.class.isAssignableFrom(type.getRawType())) return null;
      final TypeAdapter<JsonElement> ea = gson.getAdapter(JsonElement.class);
      final TypeAdapter<InformacionesAdicionales> ta = gson.getDelegateAdapter(this, TypeToken.get(InformacionesAdicionales.class));
      return (TypeAdapter<T>) new TypeAdapter<InformacionesAdicionales>() {
        @Override public void write(JsonWriter out, InformacionesAdicionales v) throws IOException { ea.write(out, ta.toJsonTree(v).getAsJsonObject()); }
        @Override public InformacionesAdicionales read(JsonReader in) throws IOException { return ta.fromJsonTree(ea.read(in)); }
      }.nullSafe();
    }
  }
  public static InformacionesAdicionales fromJson(String s) throws IOException { return JSON.getGson().fromJson(s, InformacionesAdicionales.class); }
  public String toJson() { return JSON.getGson().toJson(this); }
}
