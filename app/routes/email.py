from flask import Blueprint, request, jsonify
from flask_mail import Message
from app import mail
from app.utils.decorators import token_required

bp = Blueprint('email', __name__)

@bp.route('/send_email', methods=['POST'])
@token_required
def send_email():
    data = request.get_json()
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')

    if not recipient or not subject or not body:
        return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400

    msg = Message(subject, sender=mail.username, recipients=[recipient])
    msg.body = body

    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'message': 'Email sent successfully'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
