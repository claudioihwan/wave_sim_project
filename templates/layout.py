def layout(content = "", script = ""):
  return f"""
    <html>
      <head>
        <title>Simulator Gelombang Transversal dan Longitudinal</title>
        <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
          
        </style>
      </head>
      <body>
        <div class="w-full min-h-screen flex flex-col items-center justify-center bg-[https://simplehomemadegifts.com/wp-content/uploads/2013/01/BlackChalkboardBackgroundSmall-1.jpg] text-white md:p-4" style="font-family: 'Poppins', sans-serif;">
          {content}
          <a href="/" class="w-full text-center font-bold mt-10">Kembali ke Home</a>
        </div>
        <script>
          {script}
        </script>
      </body>
    </html>
  """
