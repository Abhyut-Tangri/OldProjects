const express = require('express');
const mongoose = require('mongoose');
const app = express();
const http = require('http').Server(app)
const io = require('socket.io')(http)
const passport = require("passport")
  , LocalStrategy = require("Passport-local").Strategy;
const sanitize = require("sanitize")
const { escapeHtml } = require('./utils')

const options = {
  useNewUrlParser: true,
  useUnifiedTopology: true
}
mongoose.connect('mongodb+srv://chat:5IPhaAGRbSRZ8gl8@cluster0.wmvhk.mongodb.net/chat', options)

const User = mongoose.model('User', {
  username: String,
  password: String
})
passport.use(new LocalStrategy(
  function (username, password, done) {
    User.findOne({ username }, function (err, user) {
      if (err) { return done(user); }
      if (!user || !user.validPassword(password)) {
        return done(null, false, {message: 'Incorrect username or password'})
      }
      return done(null, user)
    })
  }
))
app.use(sanitize.middleware)
app.use(express.urlencoded( {extended: true} ))
app.use(express.static("public"))
app.set("view engine", "ejs")

app.get("/", (req, res) => {
  res.render("index")
})

app.get("/chat", (req, res) => {
  res.render("chat")
})

app.route("/admin")
  .get((req, res) => {
    res.render('admin')
  })
  .post((req, res) => {
    const {username, password} = req.body;
    console.log(username)
    const newUser = new User({
      username,
      password
    })
    console.log(req.body)
    console.log(newUser)
    newUser.save()
    res.send('good')
  })

app.route("/signup")
  .get((req, res) => {

  })

app.use((req, res) => {
  const {url} = req;
  res.render('404', {
    url
  })
})

io.on("connection", socket => {
  socket.on("msg", data => {
    const safe_data = escapeHtml(data.data)
    socket.broadcast.emit("chat", {
      msg: safe_data
    })
  })
})

http.listen(3000);
