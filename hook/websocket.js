WebSocket.prototype.senda = WebSocket.prototype.send;
WebSocket.prototype.send = function (data){
 console.info("Hook WebSocket", data);
 return this.senda(data)
}
