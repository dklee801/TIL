# jQuery

jQuery CDN을 이용하면 jQuery 코드를 바로 사용가능

```html
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        
        <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous">
        
        </script>
        <script src = "js/05_jQuery.js"></script>
```



### Selector (선택자)



##### 1. universal selector (전체 선택자)

```javascript
$("*").css("color", "red")
```

- `*`  : universal selector : 모든 element 선택
- .css : 스타일 변경



##### 2. tag selector (태그 선택자)

```javascript
$("li").remove()
```

- li 에 해당되는 태그 전부 찾음



##### 3. 아이디 선택자(id selector)

```javascript
$("#id_1").text("제주")
```

- `#` : id를 의미
- .text() : 인자가 없으면 해당 값을 알아오기
- .text(x) : 인자가 잇으면 x로 값을 변경



##### 4. 클래스 선택자( class selector), class는 id와 달리 중복해서 부여가능

```javascript
$(".region").css("background-color","yellow")
```

- `.class`



##### 5. 구조 선택자( 자식/ 후손 선택자)

```javascript
$("ol > li").css("color","steelblue")
$("div li").css("color","pink")
```

- `>` : 자식 선택자

- ` ` : 공백은 후손을 지칭



##### 5-1. 특정 자식 선택

- 첫번째 자식 선택

```javascript
$("ol > li.myList:first").text()
```

- 마지막 자식 선택

```javascript
$("ol > li.myList:last").text()
```

- 몇번째 순번의 자식 선택

```javascript
$("ol > li.myList:nth-child(1)").text()
```

- 특정 태그 가진 자식 선택

```javascript
$("ol > li.myList:first +li").text()
```



##### 6. 구조 선택자 (형제 선택자)

```javascript
$("#id_1 + li").remove()
$("#hong ~ li").remove()
```

- `+` : 바로 뒤에 나오는 형제
- `~` : 아이디 뒤에 나오는 모든 형제



##### 7. 속성 선택자

```javascript
$("[id]").css("color", "yellow")
$("[id = idx_1]").css("color", "yellow")
```

- `[ x ]` : x  속성을 가지고 있는 것 전부
- `[x = y]` : x = y를 가지고 있는