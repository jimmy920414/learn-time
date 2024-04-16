function myDiff(a, b) {
    if (a > b) {
        return a-b
    }
    else {
        return b-a
    }
   }
   function displayInfo() {
    let now=new Date();
    document.getElementById('display_area').innerHTML
    = now.getFullYear() + '/' + (now.getMonth()+1 ) + '/' + now.getDate();
   }