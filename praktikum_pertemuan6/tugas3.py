PASSWORD_BENAR = "python123"
password_input = "" 

while password_input != PASSWORD_BENAR:
    password_input = input("Masukkan kata sandi Anda: ")
    
    if password_input != PASSWORD_BENAR:
        print("Password salah. Silakan coba lagi.")

print("Password Benar!")