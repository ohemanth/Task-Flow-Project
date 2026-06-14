document.addEventListener("DOMContentLoaded", () => {
    const root = document.documentElement;
    const loader = document.getElementById("loader");
    const savedTheme = localStorage.getItem("taskflow-theme") || "dark";
    root.setAttribute("data-theme", savedTheme);
    setTimeout(() => loader?.classList.add("loaded"), 350);

    document.querySelectorAll(".toast").forEach((toastEl) => {
        bootstrap.Toast.getOrCreateInstance(toastEl).show();
    });

    const themeToggle = document.getElementById("themeToggle");
    themeToggle?.addEventListener("click", () => {
        const nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", nextTheme);
        localStorage.setItem("taskflow-theme", nextTheme);
        const icon = themeToggle.querySelector("i");
        icon.className = nextTheme === "dark" ? "fa-solid fa-moon" : "fa-solid fa-sun";
    });

    const sidebar = document.querySelector(".sidebar");
    document.getElementById("mobileMenu")?.addEventListener("click", () => {
        sidebar?.classList.toggle("open");
    });

    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.content;
    const taskList = document.getElementById("taskList");
    const noResults = document.getElementById("noResults");
    const filterControls = ["taskSearch", "categoryFilter", "priorityFilter", "statusFilter"]
        .map((id) => document.getElementById(id))
        .filter(Boolean);

    function filterTasks() {
        const search = document.getElementById("taskSearch")?.value.toLowerCase().trim() || "";
        const category = document.getElementById("categoryFilter")?.value || "";
        const priority = document.getElementById("priorityFilter")?.value || "";
        const status = document.getElementById("statusFilter")?.value || "";
        let visible = 0;

        document.querySelectorAll(".task-card").forEach((card) => {
            const matches = (!search || card.dataset.title.includes(search))
                && (!category || card.dataset.category === category)
                && (!priority || card.dataset.priority === priority)
                && (!status || card.dataset.status === status);
            card.classList.toggle("d-none", !matches);
            if (matches) visible += 1;
        });

        noResults?.classList.toggle("d-none", visible !== 0);
    }

    filterControls.forEach((control) => control.addEventListener("input", filterTasks));

    document.querySelectorAll(".toggle-form").forEach((form) => {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            const response = await fetch(form.action, {
                method: "POST",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": csrfToken,
                },
                body: new FormData(form),
            });
            if (!response.ok) {
                form.submit();
                return;
            }
            const payload = await response.json();
            const card = form.closest(".task-card");
            const dot = form.querySelector(".complete-dot");
            const title = card?.querySelector("h3");
            card.dataset.status = payload.completed ? "completed" : "pending";
            dot?.classList.toggle("done", payload.completed);
            title?.classList.toggle("text-decoration-line-through", payload.completed);
            title?.classList.toggle("opacity-75", payload.completed);
            showLocalToast(payload.message || "Task updated.");
            filterTasks();
        });
    });

    let draggedCard = null;
    taskList?.addEventListener("dragstart", (event) => {
        draggedCard = event.target.closest(".task-card");
        draggedCard?.classList.add("dragging");
    });

    taskList?.addEventListener("dragend", async () => {
        draggedCard?.classList.remove("dragging");
        draggedCard = null;
        const ids = [...taskList.querySelectorAll(".task-card")].map((card) => card.dataset.taskId);
        if (!ids.length) return;
        await fetch("/tasks/reorder", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({ ids }),
        });
    });

    taskList?.addEventListener("dragover", (event) => {
        event.preventDefault();
        const afterElement = getDragAfterElement(taskList, event.clientY);
        if (!draggedCard) return;
        if (afterElement == null) {
            taskList.appendChild(draggedCard);
        } else {
            taskList.insertBefore(draggedCard, afterElement);
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.target.matches("input, textarea, select")) return;
        if (event.key.toLowerCase() === "n") {
            window.location.href = "/tasks/add";
        }
        if (event.key === "/") {
            event.preventDefault();
            document.getElementById("taskSearch")?.focus();
        }
    });
});

function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll(".task-card:not(.dragging):not(.d-none)")];
    return draggableElements.reduce((closest, child) => {
        const box = child.getBoundingClientRect();
        const offset = y - box.top - box.height / 2;
        if (offset < 0 && offset > closest.offset) {
            return { offset, element: child };
        }
        return closest;
    }, { offset: Number.NEGATIVE_INFINITY }).element;
}

function showLocalToast(message) {
    const container = document.querySelector(".toast-container");
    if (!container) return;
    const toast = document.createElement("div");
    toast.className = "toast taskflow-toast text-bg-primary border-0";
    toast.setAttribute("role", "alert");
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    container.appendChild(toast);
    const instance = bootstrap.Toast.getOrCreateInstance(toast, { delay: 2500 });
    instance.show();
    toast.addEventListener("hidden.bs.toast", () => toast.remove());
}
