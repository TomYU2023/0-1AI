// 定义一个函数，用于改变元素颜色
function changeColor() {
    var header = document.getElementById('header'); // 获取页面中的标题元素
    if (header.style.color == 'blue') { // 如果当前颜色是蓝色
        header.style.color = 'red'; // 改变颜色为红色
    } else {
        header.style.color = 'blue'; // 否则改回蓝色
    }
}
