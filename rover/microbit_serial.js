serial.onDataReceived(serial.delimiters(Delimiters.Hash), function () {
    const command = serial.readUntil(serial.delimiters(Delimiters.Hash));
    console.log("Got data: " + command);

    switch (command) {
        case "reset":
            // reset();
            // input.temperature()
            break;
        case "reqAll":

            break;
        case "reqTemp":
            const msg = 't:' + input.temperature();
            serial.writeString(msg);
            serial.writeLine(serial.delimiters(Delimiters.Hash));
            break;
    }



})

serial.writeLine("Hellow")
basic.forever(function () {

})

