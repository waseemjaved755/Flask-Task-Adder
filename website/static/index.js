function deleteTask(taskId) {
    fetch("/deletetask", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ taskId: taskId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}
