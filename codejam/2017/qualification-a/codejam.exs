# run like `cat A-large-practice.in | elixirc codejam.exs`

Code.compiler_options(ignore_module_conflict: true)

defmodule Reader do
  def read_line() do
    case IO.read(:stdio, :line) do
      :eof -> ""
      {:error, reason} -> IO.puts "Error: #{reason}"
      data -> data
    end
  end
end

defmodule CodeJam do
  def do_problem() do
      {n, _} = Integer.parse(Reader.read_line())
      solve_line(1, n)
  end

  defp solve_line(i, n) when i > n do
    nil
  end

  defp solve_line(i, n) do
    [pancake_string, k_str]= String.split(Reader.read_line(), " ")
    {k, _} = Integer.parse(k_str)
    flips = Pancakes.count_flips(pancake_string, k)
    if flips == -1 do
      IO.puts "Case ##{i}: IMPOSSIBLE"
    else
      IO.puts "Case ##{i}: #{flips}"
    end
    solve_line(i+1, n)
  end
end

defmodule Pancakes do
  def count_flips(pancake_string, k) do
    flips(String.graphemes(pancake_string), k)
  end

  # TODO: length(seq) runs in O(n) time
  defp flips(seq, k) when length(seq) < k do
    case all_happy_side(seq) do
      true -> 0
      false -> -1
    end
  end

  defp flips([head | tail], k) do
    case head do
      "+" -> flips(tail, k)
      "-" ->
        # we must flip the first pancake
        case flips(first_k_flipped(tail, k-1), k) do
          -1 -> -1
          f -> f + 1
        end
    end
  end

  defp first_k_flipped([], _) do
    []
  end

  defp first_k_flipped(seq, k) when k == 0 do
    seq
  end

  defp first_k_flipped([head | tail], k) do
    [flip(head) | first_k_flipped(tail, k-1)]
  end

  defp flip(pancake) do
    case pancake do
      "+" -> "-"
      "-" -> "+"
    end
  end

  defp all_happy_side([]) do
    true
  end

  defp all_happy_side([head | tail]) do
    case head do
      "+" -> all_happy_side(tail)
      "-" -> false
    end
  end
end

CodeJam.do_problem()

#IO.puts Pancakes.count_flips("---+-++-", 3)
#IO.puts Pancakes.count_flips("+++++", 4)
#IO.puts Pancakes.count_flips("-+-+-", 4)
