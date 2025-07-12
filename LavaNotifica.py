import tkinter as tk
from tkinter import Canvas, Label, Button
import time

class LavaNotificaVisual:
    def __init__(self, root):
        # Inicializa a interface principal
        self.root = root
        self.root.title("Simulação LavaNotifica - Brejão UFLA")

        # Cria o canvas para desenhar os elementos gráficos
        self.canvas = Canvas(root, width=700, height=450, bg='white')
        self.canvas.pack()

        # Estado inicial dos sensores e notificações
        self.sensor_active = False
        self.inactive_time = 0
        self.notification_sent = False
        self.last_update = time.time()

        self.notification_duration = 5  # segundos que a notificação fica visível
        self.notification_timer = 0

        # Tempo de inatividade para disparar notificação
        self.inactive_threshold = 10  # segundos

        # Desenha os elementos estáticos da interface
        self.draw_machine()
        self.draw_sensor()
        self.draw_cellphone()
        self.draw_status_labels()

        # Botão para ativar/desativar o sensor de vibração
        self.toggle_btn = Button(root, text="Ativar Vibração (SW-420)", command=self.toggle_sensor)
        self.toggle_btn.pack(pady=10)

        # Inicia o loop de atualização da interface
        self.update_loop()

    def draw_machine(self):
        # Desenha a máquina de lavar como um retângulo com texto
        c = self.canvas
        self.machine_rect = c.create_rectangle(50, 50, 250, 200, fill="#a2d2ff", outline="#00509e", width=3)
        self.machine_text = c.create_text(150, 125, text="Máquina de Lavar\nEstado: Parada", font=("Arial", 14), fill="#003566")

    def draw_sensor(self):
        # Desenha o sensor SW-420 como um círculo
        c = self.canvas
        self.sensor_circle = c.create_oval(280, 90, 320, 130, fill="gray", outline="black", width=2)
        self.sensor_label = c.create_text(300, 60, text="Sensor SW-420", font=("Arial", 12))

    def draw_cellphone(self):
        # Desenha o celular e a área de notificação
        c = self.canvas
        self.phone_body = c.create_rectangle(500, 50, 650, 300, fill="#222222", outline="#000000", width=3)
        self.phone_screen = c.create_rectangle(510, 60, 640, 290, fill="#ffffff", outline="#444444")

        # Notificação (inicialmente oculta)
        self.notification_bg = c.create_rectangle(520, 70, 630, 110, fill="#0088cc", outline="#005577", width=2, state='hidden')
        self.notification_text = c.create_text(575, 90, text="LavaNotifica:\nCiclo concluído!", font=("Arial", 11, "bold"), fill="white", state='hidden')

    def draw_status_labels(self):
        # Cria labels para mostrar o status e tempo de inatividade
        self.status_label = Label(self.root, text="Status: Máquina parada", font=("Arial", 13))
        self.status_label.pack()

        self.timer_label = Label(self.root, text="Tempo inativo: 0 s", font=("Arial", 12))
        self.timer_label.pack()

    def toggle_sensor(self):
        # Alterna o estado do sensor de vibração
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
        # Exibe a notificação no celular
        c = self.canvas
        c.itemconfigure(self.notification_bg, state='normal')
        c.itemconfigure(self.notification_text, state='normal')
        self.notification_timer = time.time()
        self.status_label.config(text="Status: Máquina parada - Notificação enviada!")

    def hide_notification(self):
        # Oculta a notificação do celular
        c = self.canvas
        c.itemconfigure(self.notification_bg, state='hidden')
        c.itemconfigure(self.notification_text, state='hidden')

    def update_loop(self):
        # Atualiza o estado da interface periodicamente
        now = time.time()
        elapsed = now - self.last_update
        self.last_update = now

        c = self.canvas

        if self.sensor_active:
            # Sensor ativo: reseta o tempo de inatividade e atualiza interface
            self.inactive_time = 0
            self.notification_sent = False

            c.itemconfig(self.sensor_circle, fill="lime green")
            c.itemconfig(self.machine_rect, fill="#7ec8ff")
            c.itemconfig(self.machine_text, text="Máquina de Lavar\nEstado: Funcionando", fill="#004080")

            self.timer_label.config(text=f"Tempo inativo: {int(self.inactive_time)} s")

            self.hide_notification()
        else:
            # Sensor inativo: conta o tempo de inatividade
            self.inactive_time += elapsed

            c.itemconfig(self.sensor_circle, fill="gray")
            c.itemconfig(self.machine_rect, fill="#a2d2ff")
            c.itemconfig(self.machine_text, text="Máquina de Lavar\nEstado: Parada", fill="#003566")

            self.timer_label.config(text=f"Tempo inativo: {int(self.inactive_time)} s")

            # Se exceder o tempo de inatividade, envia notificação
            if self.inactive_time >= self.inactive_threshold and not self.notification_sent:
                self.notification_sent = True
                self.show_notification()

        # Controla o tempo de exibição da notificação
        if self.notification_sent:
            if time.time() - self.notification_timer > self.notification_duration:
                self.hide_notification()

        # Agenda próxima atualização
        self.root.after(200, self.update_loop)

if __name__ == "__main__":
    # Inicializa a aplicação Tkinter
    root = tk.Tk()
    app = LavaNotificaVisual(root)
    root.mainloop()