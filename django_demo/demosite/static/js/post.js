const msg_b = document.getElementById('get_message')
const msg_t = document.getElementById('text_message')
const board = document.getElementById('board')
const msg_list = []

msg_b.addEventListener('click', function(){
    /*console.log('click~')*/
    /*window.alert('click~')*/
    console.log(msg_t.value)
    /*msg_board = `
    <div class="sub_board">
        <p class="a1"> &gt;&gt;&gt;</p>
        <p class="a2">${msg_t.value}</p>
        <hr>
    </div>
    `*/    
    msg_list.push({
        message: msg_t.value,
    })
    let msg_board = ''
    msg_list.forEach(function(item){
        msg_board = msg_board + `
        <div class="sub_board">
            <p class="a1"> &gt;&gt;&gt;</p>
            <p class="a2">${item.message}</p>
            <hr>
        </div>
        `
    })
    board.innerHTML = msg_board
})