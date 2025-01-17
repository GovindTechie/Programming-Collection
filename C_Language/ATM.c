#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

// Function prototypes
void atm();
void displayWelcomeMessage();
void processCardTransaction(int *m_pin, int *amount);
void cashWithdraw(int *m_pin, int *amount);
void moneyTransfer(int *m_pin);
void checkBalance(int *m_pin, int amount);
void changePin(int *m_pin);
void miniStatement(int *m_pin);
void thanks();
void selectAccount();
void scanQRTransaction();

int main() {
    atm();
    return 0;
}

void atm() {
    time_t t;
    time(&t);
    int m_pin = 1699, amount = 200000;
    int option;

    displayWelcomeMessage();

    while (1) {
        printf("\nPlease choose an option:\n1. Card\n2. Scan QR\nEnter your choice: ");
        scanf("%d", &option);

        if (option == 1) {
            processCardTransaction(&m_pin, &amount);
        } else if (option == 2) {
            scanQRTransaction();
        } else {
            printf("\nInvalid option. Please try again.\n");
        }
    }
}

void displayWelcomeMessage() {
    time_t t;
    time(&t);
    printf("ATM ID: P3ENPE36\nLocation: Pune\n\n");
    printf("Good Morning\n%s\nWelcome to ATM GOVIND_KHEDKAR (7796010736)\n", ctime(&t));
    printf("\nWe have only English language\n");
}

void processCardTransaction(int *m_pin, int *amount) {
    char query;

    printf("\nPlease insert your card.\n");
    while (1) {
        printf("\nChoose an option:\n");
        printf("a. Cash Withdraw\nb. Money Transfer\nc. Check Balance\nd. Change PIN\ne. Cancel\nf. Mini Statement\nEnter your choice: ");
        scanf(" %c", &query);

        switch (query) {
            case 'a':
                cashWithdraw(m_pin, amount);
                break;
            case 'b':
                moneyTransfer(m_pin);
                break;
            case 'c':
                checkBalance(m_pin, *amount);
                break;
            case 'd':
                changePin(m_pin);
                break;
            case 'e':
                printf("Transaction cancelled.\n");
                exit(0);
            case 'f':
                miniStatement(m_pin);
                break;
            default:
                printf("Invalid option. Please try again.\n");
        }
    }
}

void cashWithdraw(int *m_pin, int *amount) {
    int pin, withdrawAmount;

    printf("\nEnter your PIN: ");
    while (1) {
        scanf("%d", &pin);
        if (pin == *m_pin) {
            selectAccount();
            printf("Enter amount to withdraw (Max 10000, multiples of 100): ");
            while (1) {
                scanf("%d", &withdrawAmount);
                if (withdrawAmount > 10000 || withdrawAmount % 100 != 0) {
                    printf("Invalid amount. Please enter an amount less than 10000 and in multiples of 100: ");
                } else {
                    printf("Processing transaction...\n");
                    printf("Transaction successful. Please collect your money.\n");
                    thanks();
                    break;
                }
            }
            break;
        } else {
            printf("Incorrect PIN. Please try again: ");
        }
    }
}

void moneyTransfer(int *m_pin) {
    int pin, transferAmount;

    printf("Enter your PIN: ");
    while (1) {
        scanf("%d", &pin);
        if (pin == *m_pin) {
            selectAccount();
            printf("Enter amount to transfer (Max 10000, multiples of 100): ");
            while (1) {
                scanf("%d", &transferAmount);
                if (transferAmount > 10000 || transferAmount % 100 != 0) {
                    printf("Invalid amount. Please enter an amount less than 10000 and in multiples of 100: ");
                } else {
                    printf("Processing transaction...\n");
                    printf("Money transferred successfully.\n");
                    thanks();
                    break;
                }
            }
            break;
        } else {
            printf("Incorrect PIN. Please try again: ");
        }
    }
}

void checkBalance(int *m_pin, int amount) {
    int pin;

    printf("Enter your PIN: ");
    while (1) {
        scanf("%d", &pin);
        if (pin == *m_pin) {
            selectAccount();
            printf("Your account balance is: %d\n", amount);
            thanks();
            break;
        } else {
            printf("Incorrect PIN. Please try again: ");
        }
    }
}

void changePin(int *m_pin) {
    int pin, newPin;

    printf("Enter your current PIN: ");
    while (1) {
        scanf("%d", &pin);
        if (pin == *m_pin) {
            printf("Enter your new PIN: ");
            scanf("%d", &newPin);
            *m_pin = newPin;
            printf("PIN changed successfully.\n");
            thanks();
            break;
        } else {
            printf("Incorrect PIN. Please try again: ");
        }
    }
}

void miniStatement(int *m_pin) {
    int pin;

    printf("Enter your PIN: ");
    while (1) {
        scanf("%d", &pin);
        if (pin == *m_pin) {
            selectAccount();
            printf("Mini Statement:\n");
            printf("Date       | Transaction ID | Description               | Debit | Credit | Balance\n");
            printf("19-06-2023 | S83405320      | UPI Transfer              | 200   | 0      | 207.13 Cr.\n");
            printf("22-06-2023 | S6808912       | UPI Transfer              | 20    | 0      | 187.13 Cr.\n");
            printf("30-06-2023 | S69038047      | Interest Paid             | 0     | 1      | 8.13 Cr.\n");
            thanks();
            break;
        } else {
            printf("Incorrect PIN. Please try again: ");
        }
    }
}

void thanks() {
    printf("\nNever give up 🥰✌️\nThank you 🙏\n");
}

void selectAccount() {
    int accountType;

    printf("\nSelect account type:\n1. Current Account\n2. Saving Account\n3. Credit Card\nEnter your choice: ");
    while (1) {
        scanf("%d", &accountType);
        if (accountType == 1 || accountType == 2 || accountType == 3) {
            break;
        } else {
            printf("Invalid choice. Please try again: ");
        }
    }
}

void scanQRTransaction() {
    printf("Scan the QR code using any UPI application (Google Pay, PhonePe, Paytm).\n");
    printf("Processing transaction...\n");
    printf("Transaction completed successfully. Please collect your money.\n");
    thanks();
}
