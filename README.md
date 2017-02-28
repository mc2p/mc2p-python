# MyChoice2Pay Python


# Overview

MyChoice2Pay Python provides integration access to the MyChoice2Pay API.

# Installation

You can install using `pip`:

    pip install --upgrade mc2p-python
    
or `easy_install`

    easy_install --upgrade mc2p-python

or to install from source, run:

    python setup.py install

# Quick Start Example

    from mc2p import MC2P
    
    mc2p = MC2PClient('KEY', 'SECRET_KEY')
    
    # Create transaction
    transaction = mc2p.Transaction({
        "currency": "EUR",
        "products": [{
            "amount": 1,
            "product": {
                "name": "Product",
                "price": 5
            }
        }]
    })
    transaction.save()
    transaction.pay_url # Send user to this url to pay

    # Get plans
    plans_paginator = mc2p.plan.list()
    plans_paginator.count
    plans_paginator.results # Application's plans
    plans_paginator.get_next_list()
    
    # Get product, change and save
    product = mc2p.Product({
        "id": "PRODUCT-ID"
    })
    product.retrieve()
    product.price = 10
    product.save()
    
    # Create and delete tax
    tax = mc2p.Tax({
        "name": "Tax",
        "percent": 5
    })
    tax.save()
    tax.delete()
    
    # Check if transaction was paid
    transaction = mc2p.Transaction({
        "id": "TRANSACTION-ID"
    })
    transaction.retrieve()
    transaction.status == 'D' # Paid
    
    # Create subscription
    subscription = mc2p.Subscription({
        "currency": "EUR",
        "plan_id": "PLAN-ID",
        "note": "Note example"
    })
    # or
    subscription = mc2p.Subscription({
        "currency": "EUR",
        "plan": {
            "name": "Plan",
            "price": 5,
            "duration": 1,
            "unit": "M",
            "recurring": true
        },
        "note": "Note example"
    })
    subscription.save()
    subscription.pay_url # Send user to this url to pay

# Exceptions
    
    from mc2p.errors import InvalidRequestError
    
    # Incorrect data
    shipping = mc2p.Shipping({
        "name": "Normal shipping",
        "price": "text" # Price must be number
    })
    try:
        shipping.save()
    except InvalidRequestError as e:
        e._message # Status code of error
        e.json_body # Info from server
        e.resource # Resource used to make the server request
        e.resource_id # Resource id requested    
