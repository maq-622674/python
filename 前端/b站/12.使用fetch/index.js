/*
ES6,无需插件支持
获取资源的接口
比XMLHttpRequest更好用
返回一个promise
避免回调
并不会因为状态码错误而reject
*/
// GET
fetch('http://127.0.0.1:9998/upload/')
.then(response=>response.json())
.then(myJson=>{
    console.log(myJson);
})
.catch(err=>{
    console.log(err);
})


//#########################################################
//POST
// const data={id:1,title:'abc'}
// fetch(url,{
//     body:JSON.stringify(data),
//     method:'POST'
// })
// .then(response=>response.json())
// .then(myJson=>{
//     console.log(myJson)
// })
// .catch(err=>{
//     console.log(err)
// })

//#########################################################
//上传JSON数据
// var url = 'https://example.com/profile';
// var data = {username: 'example'};

// fetch(url, {
//   method: 'POST', // or 'PUT'
//   body: JSON.stringify(data), // data can be `string` or {object}!
//   headers: new Headers({
//     'Content-Type': 'application/json'
//   })
// }).then(res => res.json())
// .catch(error => console.error('Error:', error))
// .then(response => console.log('Success:', response));


//#########################################################
//上传单个文件
// var formData = new FormData();
// var fileField = document.querySelector("input[type='file']");

// formData.append('username', 'abc123');
// formData.append('avatar', fileField.files[0]);

// fetch('https://example.com/profile/avatar', {
//     method: 'PUT',
//     body: formData
// })
// .then(response => response.json())
// .catch(error => console.error('Error:', error))
// .then(response => console.log('Success:', response));


//#########################################################
//上传多个文件
// var formData = new FormData();
// var photos = document.querySelector("input[type='file'][multiple]");

// formData.append('title', 'My Vegas Vacation');
// // formData 只接受文件、Blob 或字符串，不能直接传递数组，所以必须循环嵌入
// for (let i = 0; i < photos.files.length; i++) {
//     formData.append('photo', photos.files[i]);
// }

// fetch('https://example.com/posts', {
//     method: 'POST',
//     body: formData
// })
// .then(response => response.json())
// .then(response => console.log('Success:', JSON.stringify(response)))
// .catch(error => console.error('Error:', error));


//####################################################
//检测是否请求成功
// fetch('flowers.jpg').then(function (response) {
//     if (response.ok) {
//         return response.blob();
//     }
//     throw new Error('Network response was not ok.');
// }).then(function (myBlob) {
//     var objectURL = URL.createObjectURL(myBlob);
//     myImage.src = objectURL;
// }).catch(function (error) {
//     console.log('There has been a problem with your fetch operation: ', error.message);
// });