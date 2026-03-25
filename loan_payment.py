python


def calculate_loan_payment(annual_interest_rate, loan_term_years, present_value):
    """
    Calculates the monthly loan payment using the standard amortization formula.

    Args:
        annual_interest_rate (float): The annual interest rate (e.g., 5 for 5%).
        loan_term_years (int): The loan term in years.
        present_value (float): The principal amount of the loan.

    Returns:
        float: The monthly loan payment amount. Returns 0 if interest rate is 0.
    """

    if annual_interest_rate == 0:
        if loan_term_years == 0:
            return 0.0  # Or raise an error, depending on desired behavior for 0 term
        return present_value / (loan_term_years * 12)

    # Convert annual interest rate to monthly decimal rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Convert loan term from years to months
    number_of_payments = loan_term_years * 12

    # Calculate the monthly payment using the loan amortization formula
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]
    numerator = (
        monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments
    )
    denominator = (1 + monthly_interest_rate) ** number_of_payments - 1

    monthly_payment = present_value * (numerator / denominator)

    return monthly_payment


if __name__ == "__main__":
    # Example Usage:
    # Loan amount: $200,000
    # Annual interest rate: 4.5%
    # Loan term: 30 years

    loan_amount = 200000
    interest_rate_percent = 4.5
    term_in_years = 30

    payment = calculate_loan_payment(interest_rate_percent, term_in_years, loan_amount)
    print(f"Loan Amount: ${loan_amount:,.2f}")
    print(f"Annual Interest Rate: {interest_rate_percent}%")
    print(f"Loan Term: {term_in_years} years")
    print(f"Monthly Payment: ${payment:,.2f}")

    # Example with 0 interest
    loan_amount_no_interest = 10000
    interest_rate_zero = 0
    term_no_interest = 5
    payment_no_interest = calculate_loan_payment(
        interest_rate_zero, term_no_interest, loan_amount_no_interest
    )
    print(f"\nLoan Amount (0% interest): ${loan_amount_no_interest:,.2f}")
    print(f"Annual Interest Rate: {interest_rate_zero}%")
    print(f"Loan Term: {term_no_interest} years")
    print(f"Monthly Payment: ${payment_no_interest:,.2f}")
