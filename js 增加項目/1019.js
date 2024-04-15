var x = 1;
$(document).ready(function () {
    $('#btnAddItem').on('click', function () {
        x = x + 1;
        displayCount();
    });
    $('#btnSubItem').on('click', function () {
        x = Math.max(0, x - 1);
        displayCount();
    });
    $('#btnReset').on('click', function () {
        x = 0;
        displayCount();
    });
});



    function displayCount() {
        
        $('#counter').text(`${x} 個項目`);

        
        $('#itemList').empty();

        //for迴圈 從1到x
        for (let i = 1; i <= x; i++) {
            const className = (i % 2 === 0) ? 'even-item' : 'odd-item';
            //利用%判斷是奇數還是偶數
            // if (i%2 === 0)(
            //     'even-item' 偶數
            // )else{
            //     'odd-item'  奇數
            // }
            $('#itemList').append(`<li class="${className}">${i}. Item</li>`);
        }
    }


