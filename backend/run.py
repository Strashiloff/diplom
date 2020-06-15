from controller import app
import webbrowser
dev=True

if __name__ == "__main__":
  if not dev:
    webbrowser.open_new('http://localhost:5000')

  app.run(debug=dev) # Убрать дебаг на проде
