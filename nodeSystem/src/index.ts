let request = new XMLHttpRequest();

request.onreadystatechange = () => {
    if(this.readyState === 4 && this.status === 200) {
        console.log(request.response);
    }
}

request.open('GET', 'http://127.0.0.1:5000/widgets/get');
request.send();