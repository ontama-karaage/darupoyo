from src.app.notify import Notifier


def test_message_is_data_for_web_and_alert_for_ios():
    message = Notifier.build_message(["t" * 30], "ぽよが洗濯したよ", "ほめにいこ", "/")
    assert message.data == {"title": "ぽよが洗濯したよ", "body": "ほめにいこ", "link": "/"}
    assert message.webpush.headers["Urgency"] == "high"
    alert = message.apns.payload.aps.alert
    assert (alert.title, alert.body) == ("ぽよが洗濯したよ", "ほめにいこ")
    assert message.apns.payload.aps.sound == "default"
    # data only for web: no top-level notification, or the browser would show it twice
    assert message.notification is None
