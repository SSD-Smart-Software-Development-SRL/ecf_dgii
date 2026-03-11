package dom.com.ssd.ecfx.client;

/**
 * Exception thrown by EcfClient for routing errors, polling timeouts,
 * and ECF processing failures.
 */
public class EcfClientException extends Exception {

    private final String messageId;
    private final String errorCode;

    public EcfClientException(String message) {
        this(message, null, null, null);
    }

    public EcfClientException(String message, Throwable cause) {
        this(message, cause, null, null);
    }

    public EcfClientException(String message, Throwable cause, String messageId, String errorCode) {
        super(message, cause);
        this.messageId = messageId;
        this.errorCode = errorCode;
    }

    /** The DGII message ID if available, null otherwise. */
    public String getMessageId() {
        return messageId;
    }

    /** The DGII error code if available, null otherwise. */
    public String getErrorCode() {
        return errorCode;
    }
}
