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

  defp solve_line(i, n) do
    cond do
      i > n -> nil
      true ->
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
end

defmodule Pancakes do
  def count_flips(pancake_string, k) do
    flips(String.graphemes(pancake_string), k)
  end

  defp flips(seq, k) do
    [head | rest] = seq
    cond do
      length(seq) < k ->
        if all_happy_side(seq) do
          0
        else
          -1
        end
      head == "+" ->
        flips(rest, k)
      true ->
        case flips(first_k_flipped(rest, k-1), k) do
          -1 -> -1
          f -> f + 1
        end
    end
  end

  defp first_k_flipped(seq, k) do
    cond do
      k == 0 -> seq
      List.first(seq) == nil -> seq
      true ->
        [_ | rest] = seq
        [flip(List.first(seq)) | first_k_flipped(rest, k-1)]
    end
  end

  defp flip(pancake) do
    case pancake do
      "+" -> "-"
      "-" -> "+"
    end
  end

  defp all_happy_side(seq) do
    case List.first(seq) do
      nil ->
        true
      "+" ->
        [_ | rest] = seq
        all_happy_side(rest)
      "-" -> false
    end
  end
end

CodeJam.do_problem()

#IO.puts Pancakes.count_flips("---+-++-", 3)
#IO.puts Pancakes.count_flips("+++++", 4)
#IO.puts Pancakes.count_flips("-+-+-", 4)
