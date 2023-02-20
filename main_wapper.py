import os
from flask import Flask, request, jsonify
from User_Details import User

app = Flask(__name__)



@app.route('/')
def index():
    return 'Welcome XYZ...!!!'

@app.route('/transfer_money', methods=['POST'])
def transfer_money():
    request.method == 'POST'
    req = request.get_json()
    sender = req.get('sender_acc')
    recipient = req.get('recipient_acc')
    amount = req.get('amount')
    if sender == recipient:
        return 'Sender and recipient cannot be the same!'
    sender_balance = MoneyTransfer.query.filter_by(sender=sender).all()
    recipient_balance = MoneyTransfer.query.filter_by(recipient=recipient).all()
    sender_total = sum([t.amount for t in sender_balance])
    recipient_total = sum([t.amount for t in recipient_balance])
    if sender_total < amount:
        return 'Insufficient funds!'
    transfer = MoneyTransfer(sender=sender, recipient=recipient, amount=amount)
    db.session.add(transfer)
    db.session.commit()
    return f'Successfully transferred {amount} from {sender} to {recipient}.'

@app.route('/updateuser/', methods=['POST'])
def update_user():
    try:
        if request.method == 'POST':
            content = request.get_json()

            email_id = content.get('email')

            mob= content.get('mobile')
            adr=content.get('address')
            print('Updated Details for : ', email_id)
            print(mob)

            upd_user_obj = User(email_id=email_id)

            if mob:
                mobile_upd = upd_user_obj.user_update_mobile(email_id, mob)

                if mobile_upd:
                    return mobile_upd, 200
                else:
                    return 'Mobile Number has been successfully updated.', 200

            elif adr:
                address_upd = upd_user_obj.user_update_addre(email_id, adr)

                if address_upd:
                    return address_upd, 200
                else:
                    return 'First Name has been successfully updated.', 200

            else:
                return 'Error! Please provide the correct input for update the user details.', 400

    except Exception as ex:
        print("Error! while Updating the user details : \n", ex)
        return "Error! while Updating the user details.", 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False, use_reloader=False)
