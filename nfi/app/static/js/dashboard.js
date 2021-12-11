function runTool(tool) {
    document.getElementById("output").innerHTML = "Please Wait..."
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (xhr.responseURL.includes("/?message")) {
                location.href = '/?message=Session+timed+out';
            }
            else {
                document.getElementById("output").innerHTML = xhr.responseText;
            }
        }
    };
    xhr.open("GET", tool, true);
    xhr.send()
    document.getElementById('tool').style.display = 'block'
}