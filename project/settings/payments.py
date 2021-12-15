import os


SALES_TEAM = []
SERVICE_TEAM = []

PRODUCT_GST_PERCENT = 18
PAYMENT_PROVIDER = 'Stripe'
KYC_GST_PAN_REQUIRED = False
CART_INVOICE_ITEM_CUSTOM_FIELD = True
SHIPPING_ADDRESS_REQUIRED = False
ON_PAYMENT_SUCCESS = 'payments.models.OnPaymentSuccess'

PAYMENT_CURRENCY = 'USD'

INVOICE_SELLER = {
    'name': 'Qux',
    'address': '1 Qux Plaza, Qux Way, Mumbai, MH',
    'gstin': '22ABCDE1703R1YZ'
}

# Stripe
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None)
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', None)
STRIPE_ENDPOINT_SECRET = os.getenv('STRIPE_ENDPOINT_SECRET', None)
# STRIPE_DOMAIN_URL should be set to http://127.0.0.1:8000/ if in dev mode
STRIPE_DOMAIN_URL = 'https://qux.dev/'
