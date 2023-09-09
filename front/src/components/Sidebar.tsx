import { useState } from "react";
export default function Sidebar() {
    let questionNum:number = 1;
    const addQuestion = async() =>{
        questionNum=+1
        const newQuestion =async () => {
        return(
            <div> вопрос {questionNum}</div>
        )
        }
    }
    return(
        <>
            <div onClick={addQuestion}><p>plus</p></div>
            <div>
                Вопрос {questionNum}
                {newQuestion}
            </div>
        </>
    )
}