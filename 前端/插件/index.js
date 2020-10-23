function box_hide(data, data1) {
    //功能:点击data隐藏data1
    data.onclick = function() {
        data1.style.display = "none";
    }
}

function box_show(data, data1) {
    //功能:点击data显示data1
    data.onclick = function() {
        data1.style.display = "block";
    }
}

function box_hide_show(data, data1) {
	
    if (is_hidden(data1)) {
        box_hide(data, data1);
    } else {    
		box_show(data, data1);
    }
}
function is_hidden(data){
	//功能:判断data处于隐藏状态还是显示状态
}
function box_click(data, data1) {

}