const sum = (a, b) => {
  console.log("point-5");
  setTimeout(
    ()=>(a+b),
    2000
  );
  console.log("point-6");
};


const asyncFx = (a, b) => {
  const promise = new Promise((res, rej) => {
    console.log("point-0");

    setTimeout(
      () => {
        console.log("point-1");
        let s1 = sum(a, b);
        console.log("point-2");
        res(s1);
        console.log("point-3");
      },
      3000);
    
      console.log("point-4");
  });
  return promise;
};


asyncFx(1, -2).then(data => {
  console.log("data = ", data);
})
.catch(err => {
  console.log("error = ", err);
});

console.log('END');
