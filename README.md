# MyChoice2Pay Python


# Overview

MyChoice2Pay Python provides integration access to the MyChoice2Pay API.

[![Build Status](https://travis-ci.org/mc2p/mc2p-python.svg?branch=master)](https://travis-ci.org/mc2p/mc2p-python)
[![Coverage Status](https://coveralls.io/repos/github/mc2p/mc2p-python/badge.svg?branch=master)](https://coveralls.io/github/mc2p/mc2p-python?branch=master)
[![Code Health](https://landscape.io/github/mc2p/mc2p-python/master/landscape.svg?style=flat)](https://landscape.io/github/mc2p/mc2p-python/master)

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
    transaction.iframe_url # Use this url to show an iframe in your site

    # Get plans
    plans_paginator = mc2p.plan.list()
    plans_paginator.count
    plans_paginator.results # Application's plans
    plans_paginator.get_next_list()
    
    # Get product, change and save
    product = mc2p.Product.get("PRODUCT-ID")
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
    transaction = mc2p.Transaction.get("TRANSACTION-ID")
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
            "recurring": True
        },
        "note": "Note example"
    })
    subscription.save()
    subscription.pay_url # Send user to this url to pay
    subscription.iframe_url # Use this url to show an iframe in your site

    # Receive a notification
    notification_data = mc2p.NotificationData(JSON_DICT_RECEIVED_FROM_MYCHOICE2PAY)
    notification_data.status == 'D' # Paid
    notification_data.transaction # Transaction Paid
    notification_data.sale # Sale generated

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
