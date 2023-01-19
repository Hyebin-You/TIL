import React, { useState } from 'react';
import ExpenseDate from './ExpenseDate'
import Card from '../UI/Card'
import './ExpenseItem.css';

function ExpenseItem(props) {
    // useState는 컴포넌트 함수 안에서 직접적으로 실행되어야 함
    // 컴포넌트 함수 내의 다른 함수 안에 작성되어서도 안됨
    const [title, setTitle] = useState(props.title);
    
    const clickHandler = () => {
        setTitle('Updated!');
        console.log(title);
    }

    return (
        <Card className="expense-item">
            <ExpenseDate date={props.date}/>
            <div className='expense-item__description'>
                <h2>{ title }</h2>
                <div className='expense-item__price'>${props.amount}</div>
            </div>
            <button onClick={clickHandler}>Change Title</button>
        </Card>
    );
}

export default ExpenseItem