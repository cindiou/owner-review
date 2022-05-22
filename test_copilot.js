// 实现Promise

// javascript:void (function(){var elContainer=document.querySelector(".deqr-item");window.addEventListener("paste",function(e){const files=e.clipboardData.files;const dataTransfer=new DataTransfer();for(const file of files){if(/^image/.test(file.type)){dataTransfer.items.add(file)}}elContainer.dispatchEvent(new DragEvent("drop",{bubbles:true,cancelable:true,dataTransfer}));
// })})();

function _(){
  const iframe=document.createElement("iframe");
  iframe.src="https://cli.im/deqr";

  iframe.contentWindow.onload=()=>console.log("Hello,World!");
  iframe.style.display="none";
  document.body.appendChild(iframe);

  console.log("=====1====")
  const elContainer=iframe.contentDocument.querySelector(".deqr-item");
  iframe.contentWindow.addEventListener("inner-paste",function(e){
    const files=e.detail;
    console.log("files=",files);
    const dataTransfer=new DataTransfer();
    for(const file of files){
      if(/^image/.test(file.type)){
        dataTransfer.items.add(file)
      }
    }
    elContainer.dispatchEvent(new DragEvent("drop",{bubbles:true,cancelable:true,dataTransfer}));
  });


  console.log("=====2====")
  window.addEventListener("paste",(e)=>{
    const detail=e.clipboardData.files;
    console.log("detail=",detail)
    iframe.contentWindow.dispatchEvent(new CustomEvent("inner-paste",{
      bubbles:true,cancelable:true,detail
    }))
  })

  iframe.contentWindow.onload=function(){
    console.log("=====3====")
    // const warnTip=iframe.ownerDocument.querySelector(".warn-tip");
    // const resultWrap=iframe.ownerDocument.querySelector(".result-wrap");
    // const observer=new iframe.contentWindow.MutationObserver((records,self)=>{
    //   records.map((r)=>{
    //     console.log("record=",r)
    //     switch(true){
    //       case warnTip && warnTip.style.display === "block" :
    //         return alert("二维码解析失败~");
    //       case resultWrap && resultWrap.style.display === "block" :
    //         iframe.ownerDocument.querySelector(".op-copy").click();
    //         return alert("已复制到剪贴板~")
    //       default:
    //         console.log("default")
    //     }
    //   })
    // });

    // console.log("=====4====")
    // for(const el of [warnTip,resultWrap,]){
    //   observer.observe(el,{
    //     "attributes":true,
    //     "attributeFilter":["style"]
    //   })
    // }
  }

  // warn-tip
  // result-wrap
  //   op-copy
}