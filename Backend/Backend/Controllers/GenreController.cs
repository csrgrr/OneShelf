using Backend.Config;
using Backend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Net.Sockets;

namespace Backend.Controllers
{
    [Route("/api/genre")]
    public class GenreController : Controller
    {

        private readonly DBArticlesContext _context;
        public GenreController(DBArticlesContext context) 
        {
            _context = context;
        }


        //C
        [HttpPost("save")]
        public async Task<ActionResult> SaveGenre([FromBody] Genres genre)
        {
            _context.Add(genre); //add to context
            await _context.SaveChangesAsync();

            return Ok(genre);
        }

 

        //R
        [HttpGet("list")]
        public async Task<ActionResult<List<Genres>>> GetGenres()
        {
            return await _context.Genres.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Genres>> ShowGendersById(int id)
        {
            var genresExist = await _context.Genres.AnyAsync(x => x.Id == id);

            if (!genresExist)
            {
                return BadRequest($"The genre with id {id} does not exist");
            }

            return await _context.Genres.Include(x => x.Article).FirstOrDefaultAsync(x => x.Id == id);
        }

        //U
        [HttpPut("/updateGenre/{id}")]
        public async Task<ActionResult> PutGenre(int id, Genres genre)
        {
            _context.Entry(genre).State = EntityState.Modified;
            await _context.SaveChangesAsync();

            return Ok(genre);
        }

        //D
        [HttpDelete("/deleteGenre/{id}")]
        public async Task<ActionResult> Delete(int id)
        {
            Genres genre = await _context.Genres.FindAsync(id);

            _context.Remove(genre);

            await _context.SaveChangesAsync();

            return NoContent();
        }


    }
}
