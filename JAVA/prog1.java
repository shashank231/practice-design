import share.Try;

public interface Pp {
    /**
     * Processes a payment for a given amount and currency.
     * 
     * @param amount a double representing the payment amount
     * @param currency a String representing the currency code (e.g., "USD")
     * @return a String representing the unique transaction ID
     */
    String processPayment(double amount, String currency);

    public static void main(String[] args) {
        System.out.println("-------------- HERE ------------------");
    }
}


// Non-public implementation class :  it is considered package-private by default. This means the class can only be accessed by other classes within the same package.
class StripePaymentProcessor implements Pp {
    @Override
    public String processPayment(double amount, String currency) {
        String transactionId = "TXN" + System.currentTimeMillis();
        System.out.println("Processing payment of " + amount + " " + currency + " through Stripe.");
        return transactionId;
    }

    public static void main(String[] args) {
        Pp paymentProcessor = new StripePaymentProcessor();
        System.out.println("-------------- HERE ------------------");
        String transactionId = paymentProcessor.processPayment(150.00, "USD");
        System.out.println("transaction_id: " + transactionId);
        Try.main(args);
    }
}