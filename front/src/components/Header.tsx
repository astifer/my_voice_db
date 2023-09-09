export default function Header(){
    let getid:number = 1;
  return (
    <>
      <div className='w-full h-10 bg-[#7A7A7A] flex items-center mt-0'>
        <div className='flex justify-between items-center w-[80%] m-auto h-inherit'>
          <p>мой голос</p>
          <div className='flex justify-between items-center'>
            <p>код опроса :{getid}</p>
            <div className='bg-[#d9d9d9] w-5 h-5 text-center items-center ml-5'>
              <p className='text-center'>лк</p>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}