$(()=>{
    let image = {};

    $.get("data.json", data=>{
        image = data;
    });

    const canvas = $("#canvas")[0].getContext("2d");

    canvas.lineCap = "round";
    canvas.lineJoin = "round";

    $(image.lines).each((_, line)=>{
        canvas.lineWidth = line.thickness;
        canvas.strokeStyle = line.color;

        canvas.moveTo(line.points[0].x, line.points[0].y);

        $(line.points).each((_, pointCollection)=>{
            canvas.lineTo(pointCollection.x, pointCollection.y);
        });

        canvas.stroke();
    });
});