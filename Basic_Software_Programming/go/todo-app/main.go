package main

import (
	"encoding/json"
	"net/http"
	"sync"

	"github.com/gorilla/mux" // Importa o pacote mux
)

// Task representa uma tarefa.
type Task struct {
	ID   string `json:"id"`
	Name string `json:"name"`
	Done bool   `json:"done"`
}

// TaskStore armazena as tarefas.
var TaskStore = struct {
	sync.RWMutex
	tasks map[string]Task
}{tasks: make(map[string]Task)}

// createTask cria uma nova tarefa.
func createTask(w http.ResponseWriter, r *http.Request) {
	var task Task
	err := json.NewDecoder(r.Body).Decode(&task)
	if err != nil || task.ID == "" || task.Name == "" {
		http.Error(w, "Invalid input", http.StatusBadRequest)
		return
	}

	TaskStore.Lock()
	TaskStore.tasks[task.ID] = task
	TaskStore.Unlock()

	w.WriteHeader(http.StatusCreated)
	json.NewEncoder(w).Encode(task)
}

// getTasks retorna todas as tarefas.
func getTasks(w http.ResponseWriter, r *http.Request) {
	TaskStore.RLock()
	defer TaskStore.RUnlock()

	tasks := make([]Task, 0, len(TaskStore.tasks))
	for _, task := range TaskStore.tasks {
		tasks = append(tasks, task)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(tasks)
}

// updateTask atualiza uma tarefa existente.
func updateTask(w http.ResponseWriter, r *http.Request) {
	var task Task
	err := json.NewDecoder(r.Body).Decode(&task)
	if err != nil || task.ID == "" {
		http.Error(w, "Invalid input", http.StatusBadRequest)
		return
	}

	TaskStore.Lock()
	defer TaskStore.Unlock()

	if _, exists := TaskStore.tasks[task.ID]; !exists {
		http.Error(w, "Task not found", http.StatusNotFound)
		return
	}

	TaskStore.tasks[task.ID] = task
	json.NewEncoder(w).Encode(task)
}

// deleteTask remove uma tarefa.
func deleteTask(w http.ResponseWriter, r *http.Request) {
	id := r.URL.Query().Get("id")

	TaskStore.Lock()
	defer TaskStore.Unlock()

	if _, exists := TaskStore.tasks[id]; !exists {
		http.Error(w, "Task not found", http.StatusNotFound)
		return
	}

	delete(TaskStore.tasks, id)
	w.WriteHeader(http.StatusNoContent)
}

func main() {
	router := mux.NewRouter() // Cria um novo roteador

	router.HandleFunc("/tasks", getTasks).Methods("GET")         // Para obter todas as tarefas
	router.HandleFunc("/tasks", createTask).Methods("POST")      // Para criar uma nova tarefa
	router.HandleFunc("/tasks/{id}", updateTask).Methods("PUT")  // Para atualizar uma tarefa existente
	router.HandleFunc("/tasks/{id}", deleteTask).Methods("DELETE") // Para deletar uma tarefa

	http.ListenAndServe(":8080", router) // Inicia o servidor HTTP com o roteador
}
