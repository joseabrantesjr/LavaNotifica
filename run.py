import tkinter as tk
from tkinter import Canvas, Label, Button
import time

class LavaNotificaVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação LavaNotifica - Brejão UFLA")

        self.canvas = Canvas(root, width=700, height=450, bg='white')
        self.canvas.pack()

        # Estado inicial
        self.sensor_active = False
        self.inactive_time = 0
        self.notification_sent = False
        self.last_update = time.time()

        self.notification_duration = 5  # segundos que a notificação fica visível
        self.notification_timer = 0

        # Parâmetro do tempo inativo para disparar notificação
        self.inactive_threshold = 10  # segundos (ajustado)

        # Desenha elementos estáticos
        self.draw_machine()
        self.draw_sensor()
        self.draw_cellphone()
        self.draw_status_labels()

        # Botão para alternar vibração
        self.toggle_btn = Button(root, text="Ativar Vibração (SW-420)", command=self.toggle_sensor)
        self.toggle_btn.pack(pady=10)

        # Loop de atualização
        self.update_loop()

    def draw_machine(self):
        c = self.canvas
        # Máquina de lavar: retângulo com texto
        self.machine_rect = c.create_rectangle(50, 50, 250, 200, fill="#a2d2ff", outline="#00509e", width=3)
        self.machine_text = c.create_text(150, 125, text="Máquina de Lavar\nEstado: Parada", font=("Arial", 14), fill="#003566")

    def draw_sensor(self):
        c = self.canvas
        # Sensor SW-420: pequeno círculo que pisca quando ativo
        self.sensor_circle = c.create_oval(280, 90, 320, 130, fill="gray", outline="black", width=2)
        self.sensor_label = c.create_text(300, 60, text="Sensor SW-420", font=("Arial", 12))

    def draw_cellphone(self):
        c = self.canvas
        # Celular simples: retângulo com tela e área de notificação
        self.phone_body = c.create_rectangle(500, 50, 650, 300, fill="#222222", outline="#000000", width=3)
        self.phone_screen = c.create_rectangle(510, 60, 640, 290, fill="#ffffff", outline="#444444")

        # Notificação (inicialmente invisível)
        self.notification_bg = c.create_rectangle(520, 70, 630, 110, fill="#0088cc", outline="#005577", width=2, state='hidden')
        self.notification_text = c.create_text(575, 90, text="LavaNotifica:\nCiclo concluído!", font=("Arial", 11, "bold"), fill="white", state='hidden')

    def draw_status_labels(self):
        # Labels abaixo do canvas para status do sistema
        self.status_label = Label(self.root, text="Status: Máquina parada", font=("Arial", 13))
        self.status_label.pack()

        self.timer_label = Label(self.root, text="Tempo inativo: 0 s", font=("Arial", 12))
        self.timer_label.pack()

    def toggle_sensor(self):
        self.sensor_active = not self.sensor_active
        if self.sensor_active:
            self.toggle_btn.config(text="Desativar Vibração (SW-420)")
            self.status_label.config(text="Status: Máquina em funcionamento")
            self.inactive_time = 0
            self.notification_sent = False
            self.hide_notification()
        else:
            self.toggle_btn.config(text="Ativar Vibração (SW-420)")
            self.status_label.config(text="Status: Máquina parada")

    def show_notification(self):
        c = self.canvas
        c.itemconfigure(self.notification_bg, state='normal')
        c.itemconfigure(self.notification_text, state='normal')
        self.notification_timer = time.time()
        self.status_label.config(text="Status: Máquina parada - Notificação enviada!")

    def hide_notification(self):
        c = self.canvas
        c.itemconfigure(self.notification_bg, state='hidden')
        c.itemconfigure(self.notification_text, state='hidden')

    def update_loop(self):
        now = time.time()
        elapsed = now - self.last_update
        self.last_update = now

        c = self.canvas

        if self.sensor_active:
            # Sensor ativo: reset timer e indica máquina vibrando
            self.inactive_time = 0
            self.notification_sent = False

            c.itemconfig(self.sensor_circle, fill="lime green")
            c.itemconfig(self.machine_rect, fill="#7ec8ff")
            c.itemconfig(self.machine_text, text="Máquina de Lavar\nEstado: Funcionando", fill="#004080")

            self.timer_label.config(text=f"Tempo inativo: {int(self.inactive_time)} s")

            self.hide_notification()
        else:
            # Sensor inativo: máquina parada, conta o tempo
            self.inactive_time += elapsed

            c.itemconfig(self.sensor_circle, fill="gray")
            c.itemconfig(self.machine_rect, fill="#a2d2ff")
            c.itemconfig(self.machine_text, text="Máquina de Lavar\nEstado: Parada", fill="#003566")

            self.timer_label.config(text=f"Tempo inativo: {int(self.inactive_time)} s")

            if self.inactive_time >= self.inactive_threshold and not self.notification_sent:
                self.notification_sent = True
                self.show_notification()

        # Controla o tempo que a notificação fica visível
        if self.notification_sent:
            if time.time() - self.notification_timer > self.notification_duration:
                self.hide_notification()

        self.root.after(200, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = LavaNotificaVisual(root)
    root.mainloop()
