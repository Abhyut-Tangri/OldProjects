const socket = io.connect()

function escapeHtml(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

$("#chat-form").on("submit", e => {
  e.preventDefault();
  const msg = e.target.firstElementChild.value;
  socket.emit("msg", {
    data: msg
  })
  $("#messages").append(`<p>You sent: ${escapeHtml(msg)}</p>`)
})

socket.on("chat", data => {
  console.log('a')
  $("#messages").append(`<p>${data.msg}</p>`)
})
