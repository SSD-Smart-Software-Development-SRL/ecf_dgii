package dom.com.ssd.ecfx.client;

import dom.com.ssd.ecfx.client.model.EcfResponse;

/**
 * Exception thrown by EcfClient for routing errors, polling timeouts,
 * and ECF processing failures.
 */
public class EcfClientException extends Exception {

    private final String messageId;
    private final String errorCode;
    private final EcfResponse response;

    public EcfClientException(String message) {
        this(message, null, null, null);
    }

    public EcfClientException(String message, Throwable cause) {
        this(message, cause, null, null);
    }

    public EcfClientException(String message, Throwable cause, String messageId, String errorCode) {
        this(message, cause, messageId, errorCode, null);
    }

    public EcfClientException(String message, Throwable cause, String messageId, String errorCode, EcfResponse response) {
        super(message, cause);
        this.messageId = messageId;
        this.errorCode = errorCode;
        this.response = response;
    }

    /** The DGII message ID if available, null otherwise. */
    public String getMessageId() {
        return messageId;
    }

    /** The DGII error code if available, null otherwise. */
    public String getErrorCode() {
        return errorCode;
    }

    /** The final ECF response when processing ended in error, null otherwise. */
    public EcfResponse getResponse() {
        return response;
    }

    /**
     * True when DGII confirmed it never received the document ({@code NotReceived}): the eNCF
     * was not used and the same eNCF may be submitted again as a new request.
     */
    public boolean canResubmit() {
        return EcfStatus.canResubmit(response);
    }
}
