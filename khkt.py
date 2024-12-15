void displaywarning (gas,fire) {  
  // Định nghĩa hàm với hai tham số: trạng thái khí gas và lửa.
  if (gas == LOW && fire == LOW) {  // Kiểm tra cả gas và lửa đều ở trạng thái LOW (có nguy hiểm).
    digitalWrite(ALERT_LED_BUZZER_PIN, HIGH);  // Bật đèn và còi báo động.
    digitalWrite(RELAY_PIN, HIGH);  // Kích hoạt role.
    servo.write(90);  // Quay động cơ servo đến 90 độ để mở cửa.
    Blynk.logEvent("canhbao", "Gas and Fire detected!");  // Gửi thông báo về điện thoại.
  } else if (gas == LOW) {  // Nếu chỉ phát hiện khí gas.
    digitalWrite(ALERT_LED_BUZZER_PIN, HIGH);  // Bật đèn và còi báo động.
    digitalWrite(RELAY_PIN, HIGH);  // Kích hoạt role.
    servo.write(90);  // Quay động cơ servo đến 90 độ để mở cửa.
    Blynk.logEvent("canhbao", "Gas detected!");  // Gửi thông báo về điện thoại.
  } else if (fire == LOW) {  // Nếu chỉ phát hiện lửa.
    digitalWrite(ALERT_LED_BUZZER_PIN, HIGH);  // Bật đèn và còi báo động.
    servo.write(90);  // Quay động cơ servo đến 90 độ để mở cửa.
    Blynk.logEvent("canhbao", "Fire detected!");  // Gửi thông báo về điện thoại.
  } else {  // Nếu không phát hiện nguy hiểm nào.
    digitalWrite(ALERT_LED_BUZZER_PIN, LOW);  // Tắt đèn và còi báo động.
    digitalWrite(RELAY_PIN, LOW);  // Tắt role.
    servo.write(0);  // Đóng cửa.
  }
}
