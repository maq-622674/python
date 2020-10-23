






//清除掉的定时器
// var TIM;
// function stop(){
//     TIM=clearInterval(TIM);
//     res();
// }
// function sta() {
//     TIM = setInterval(function() {  
//         console.log("1123")
//        stop();
//     }, 1000)
// }
// function res(){
//     sta();
// }
// res();




var TIM;
class Ding{
    constructor(){
    }
    sta(aaa){
        TIM=setInterval(function(){
            aaa
            this.stop();
        },1000)
    }
    stop(){   
        TIM=clearInterval(TIM);
        this.res();
    }
    res(bbb){
        console.log(bbb);
        this.sta(bbb);
    }

}
function bbb(){
    console.log("123")
}
aaa=new Ding();
aaa.res(bbb);








// function res() {        
//     var tim;
//     function sta() {
//         tim = setInterval(function() {
            
//            stop();
//         }, 1000)
//     }
//     function stop() {
//         tim = clearInterval(tim);
//         sta();
//     }
//     sta();
// }
// res();

//没有清除掉的定时器
// function res1() {     
//     var tim;
//     tim=setTimeout(function(){
//         res1();
//     },1000) 
//     console.log("没有清掉定时器的个数:",tim);    
// }
// res1();