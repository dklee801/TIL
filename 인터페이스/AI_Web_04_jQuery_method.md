# 04 jQuery_method



event : 사용자가 행하는 모든 행위

```javascript
$(document).ready(function set_active() {
    // 현재 이벤트가 발생된 이벤트 소스에 css를 적용
    // 이벤트 소스 : 이벤트가 발생된 element -> this
   $("ul > li").on("mouseover",function () {
       $(this).addClass("mystyle")
   })
    $("ul > li").on("mouseleave",function () {
        $(this).removeClass("mystyle")
    })

})
```



#### 텍스트 출력 : `.text()` / `.html()`

```javascript
    $("#myDiv").html("<h1>이것은 소리없는 아우성</h1>")
```

- `.text()` : 괄호 안의 모든 내용을 텍스트로 출력
- `.html()` : 괄호 안의 텍스트를 출력하되, 태그 <> 를 적용해 추력



#### 후손 삭제: `.empty()` / `.remove` 

```javascript
$("#deletediv").empty()
```

- `empty` : 자신은 남아 있고 후손만 삭제
- `remove`: 자신을 포함해서 후손들 모두 삭제



#### 없는 태그 만들기

```javascript
function add_list() {
    //없는 태그 만들기
    // <li class = "mystyle"> 박길동 </li>
    // $("<li></li>").text("박길동").attr("class","mystyle")
    var my_li = $("<li></li>").text("박길동").addclass("mystyle")
    // 태그를 생성한다음 원하는 위치에 가져다 붙임.
    // 1. append() : 자식으로 붙이고 맨 마지막에 자식으로추가
    $("ul").append(my_li)
    // 2. prepend() : 자식으로 붙이고 첫번째 자식으로 추가
    $("ul").prepend(my_li)
    // 3. afrer() : 형제로 붙이고 다음 형제로 추가
    $("ul > li:nth-child(3)").after(my_li)
    // 4. before() : 형제로 붙이고 바로 이전 형제로 붙임.
    $("ul > li:last").before(my_li)
}
```